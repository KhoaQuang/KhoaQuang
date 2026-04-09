import { test, expect } from '@playwright/test';

test.describe('Exercise 1: Practice Test Automation', () => {
    test('Test Case 1: Positive Login Test', async ({ page }) => {
        await page.goto('https://practicetestautomation.com/practice-test-login/')
        await page.getByRole('textbox', { name: 'Username' }).fill('student')
        await page.getByRole('textbox', { name: 'Password' }).fill('Password123')
        await page.getByRole('button', { name: 'Submit' }).click()
        await expect(page).toHaveURL(/logged-in-successfully/)
        const message = page.getByText('Congratulations')
        await expect(message).toBeVisible()
        const text = await message.innerText()
        console.log('Expected text: ', text)
        await expect(page.getByText('Log out')).toBeVisible()
    });

    test('Test Case 2: Negative Username Test', async ({ page }) => {
        await page.goto('https://practicetestautomation.com/practice-test-login/')
        await page.getByRole('textbox', { name: 'Username' }).fill('incorrectUser')
        await page.getByRole('textbox', { name: 'Password' }).fill('Password123')
        await page.getByRole('button', { name: 'Submit' }).click()
        const message = page.locator('#error')
        await expect(message).toBeVisible()
        const text = await message.innerText()
        console.log('The error message text is: ', text)
    });

    test('Test Case 3: Negative Password Test', async ({ page }) => {
        await page.goto('https://practicetestautomation.com/practice-test-login/')
        await page.getByRole('textbox', { name: 'Username' }).fill('student')
        await page.getByRole('textbox', { name: 'Password' }).fill('incorrectPassword')
        await page.getByRole('button', { name: 'Submit' }).click()
        const message = page.locator('#error')
        await expect(message).toBeVisible()
        const text = await message.innerText()
        console.log('The error message text is: ', text)
    });
});