import { useState } from '#app';

export const useAppTheme = () => {
    // Initialize with 'system' during SSR
    // It will resolve to 'dark' or 'light' on the client after hydration
    const theme = useState('appTheme', () => 'system');

    return theme;
};
