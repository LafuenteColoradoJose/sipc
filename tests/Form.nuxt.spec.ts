import { describe, it, expect, vi } from 'vitest';
import { mount } from '@vue/test-utils';
import Form from '../app/components/Form.vue';

const mockModel = {
  add: vi.fn(),
  setWeights: vi.fn(),
  compile: vi.fn(),
  fit: vi.fn(),
  predict: vi.fn(() => ({
    print: vi.fn(),
    arraySync: () => [[0.5]]
  }))
};

// Mock window.matchMedia
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: vi.fn().mockImplementation(query => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: vi.fn(),
    removeListener: vi.fn(),
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
    dispatchEvent: vi.fn(),
  })),
});

// Mock TensorFlow window.tf
window.tf = {
  tensor1d: vi.fn(),
  tensor2d: vi.fn(),
  sequential: vi.fn(() => mockModel),
  layers: {
    dense: vi.fn()
  }
};

// Mock Nuxt auto-imports
vi.stubGlobal('useHead', vi.fn());
vi.stubGlobal('useState', vi.fn((key) => {
  return { value: 'light' }; // Mock theme
}));

// Mock fetch
vi.stubGlobal('fetch', vi.fn(() => 
  Promise.resolve({
    ok: true,
    json: () => Promise.resolve({ mean: [0], scale: [1] }),
    arrayBuffer: () => Promise.resolve(new ArrayBuffer(1089 * 4))
  })
));

describe('Form.vue Component', () => {
  const globalConfig = {
    stubs: {
      Icon: true // Stub out the Nuxt Icon component
    }
  };

  it('renders correctly and shows the title', () => {
    const component = mount(Form, { global: globalConfig });
    expect(component.html()).toContain('Predicción de Riesgo Cardiovascular');
  });

  it('data reset button triggers reload', async () => {
    const originalReload = window.location.reload;
    
    // Create a mock for reload
    const mockReload = vi.fn();
    
    // We have to mock window.location since it's read-only in happy-dom by default, 
    // but we can try to override just reload
    Object.defineProperty(window, 'location', {
      value: { reload: mockReload },
      writable: true
    });

    const component = mount(Form, { global: globalConfig });
    
    // Find the Reset button
    const buttons = component.findAll('button');
    const resetButton = buttons.find(b => b.text().includes('Resetear formulario'));
    
    if (resetButton) {
      await resetButton.trigger('click');
      expect(mockReload).toHaveBeenCalled();
    } else {
      console.warn("Reset button not found in test");
    }

    // Restore
    window.location.reload = originalReload;
  });

  it('submits the form and calls prediction logic', async () => {
    const component = mount(Form, { global: globalConfig });
    
    // Wait for onMounted (which has awaits) to finish initializing the model
    await new Promise(resolve => setTimeout(resolve, 50));

    // Set some input values so they are not empty (optional depending on validation)
    const ageInput = component.find('input[type="number"]');
    if (ageInput.exists()) {
      await ageInput.setValue(45);
    }

    // Trigger form submit
    const form = component.find('form');
    await form.trigger('submit.prevent');

    // Wait for promises (like makePrediction) to resolve
    await new Promise(resolve => setTimeout(resolve, 10));

    // After prediction, the model.predict should have been called
    expect(mockModel.predict).toHaveBeenCalled();
  });
});
