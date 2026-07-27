import { describe, it, expect, vi } from 'vitest';
import { mount } from '@vue/test-utils';
import Advise from '../app/components/Advise.vue';
import Footer from '../app/components/Footer.vue';
import NavBar from '../app/components/NavBar.vue';
import Title from '../app/components/Title.vue';
import Header from '../app/components/Header.vue';

// Mock Nuxt auto imports
vi.stubGlobal('useAppTheme', vi.fn(() => ({
  theme: { value: 'light' },
  toggleTheme: vi.fn()
})));

const globalConfig = {
  stubs: {
    Icon: true,
    NuxtLink: true,
    UContainer: true,
    UTooltip: true,
    UButton: true
  }
};

describe('Simple Components', () => {
  it('renders Advise component', () => {
    const wrapper = mount(Advise, { global: globalConfig });
    expect(wrapper.exists()).toBe(true);
  });

  it('renders Footer component', () => {
    const wrapper = mount(Footer, { global: globalConfig });
    expect(wrapper.exists()).toBe(true);
  });

  it('renders NavBar component', () => {
    const wrapper = mount(NavBar, { global: globalConfig });
    expect(wrapper.exists()).toBe(true);
  });

  it('renders Title component', () => {
    const wrapper = mount(Title, { global: globalConfig });
    expect(wrapper.exists()).toBe(true);
  });

  it('renders Header component', () => {
    const wrapper = mount(Header, { global: globalConfig });
    expect(wrapper.exists()).toBe(true);
  });
});
