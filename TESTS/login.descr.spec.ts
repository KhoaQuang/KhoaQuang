import { devices } from '@playwright/test';
import { test, expect } from '../fixtures/test-fixtures';
import { LoginPage } from '../pages/login.page';
// import { ENV } from '../utils/env';

test.describe('Login Tests', () => {

  test.describe('Mobile - iPhone', () => {
    const iPhone = devices['iPhone 14 Pro'];

    test.use({ ...iPhone });

    test('Login success on Mobile', async ({ loginPage, page }) => {
      await loginPage.goto();
      await loginPage.login();
      await loginPage.logout();

      await expect(page).toHaveURL(/iview/);
    });
  });

  test('Login success on Desktop', async ({ loginPage, page }) => {
    await loginPage.goto(); 
    await loginPage.login();  
    await loginPage.logout();

    await expect(page).toHaveURL(/iview/);
  });

});