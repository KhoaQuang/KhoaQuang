// import { devices } from '@playwright/test';
// import { test, expect } from '../fixtures/test-fixtures';
// import { LoginPage } from '../pages/login.page';
// // import { ENV } from '../utils/env';

// const iPhone = devices['iPhone 14 Pro Max'];
// test.use({ ...iPhone });
// // test('Login success on Mobile (iPhone 14 Pro Max) using ENV', async ({ loginPage, page }) => {
// //   // const loginPage = new LoginPage(page);
// //   try {
// //     await loginPage.goto();
// //     await loginPage.login();
// //     await loginPage.logout();
// //     await expect(page).toHaveURL(/iview/);
// //     console.log('Login success on Mobile (iPhone 14 Pro Max) using ENV');
// //   } catch (error) {
// //     throw error;
// //   }
// // });

// test('Login success on Desktop using ENV', async ({ page }) => {
//   const loginPage = new LoginPage(page);
//   try {
//     await loginPage.goto(); 
//     await loginPage.login();  
//     await loginPage.logout();
//     await expect(page).toHaveURL(/iview/);
//     console.log('Login success on Desktop using ENV');
//   } 
//   catch (error) {
//     throw error;
//   }
// });

import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/login.page';
import loginData from '../data/loginData.json';

test.describe('Login Data Driven', () => {

  loginData.forEach((data, index) => {
    test.describe(`User ${index}`, () => {
      test(`With ${data.username}`, async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.goto();
        await loginPage.login(data.username, data.password);

        if (data.expected === 'success') {
          await expect(page).toHaveURL(/iview/);
        } else {
          await expect(page.locator('.error')).toBeVisible();
        }

      });

    });
  });

});