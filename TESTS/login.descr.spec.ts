import { devices } from '@playwright/test';
import { test, expect } from '../fixtures/test-fixtures';
import { LoginPage } from '../pages/login.page';
// import { ENV } from '../utils/env';

const iPhone = devices['iPhone 17 Pro Max'];
test.use({ ...iPhone });
test.describe('Login Tests', () => {
    test('Login success on Mobile (iPhone 17 Pro Max) using ENV', async ({ loginPage, page }) => {
        try {
            await loginPage.goto();
            await loginPage.login();
            await loginPage.logout();
            await expect(page).toHaveURL(/iview/);
            console.log('Login success on Mobile (iPhone 17 Pro Max) using ENV');
        } 
        catch (error) {
            throw error;
        }

        });
    
    test('Login success on Desktop using ENV', async ({ loginPage, page }) => {
        try {
            await loginPage.goto(); 
            await loginPage.login();  
            await loginPage.logout();
            await expect(page).toHaveURL(/iview/);
            console.log('Login success on Desktop using ENV');
        } 
        catch (error) {
            throw error;
        }
        });    

}); 