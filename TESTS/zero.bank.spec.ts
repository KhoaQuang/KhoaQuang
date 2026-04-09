import { test, expect } from '@playwright/test';

test.describe('Exercise 2: Zero Bank Application', () => {
    test('Test Case 1: Transfer Funds', async ({ page }) => {
        await page.goto('http://zero.webappsecurity.com/index.html')
        await page.getByText('Signin').click()
        await page.getByRole('textbox', { name: 'Login' }).fill('username')
        await page.getByRole('textbox', { name: 'Password' }).fill('password')
        await page.getByRole('button', { name: 'Sign in' }).click()
        await page.waitForLoadState("networkidle")
        await page.waitForTimeout(3000)
        await page.goto('http://zero.webappsecurity.com/bank/transfer-funds.html');
        const tmmp = page.locator('#transfer_funds_tab')
        await expect(tmmp).toHaveClass('active')
        console.log('The Transfer Funds tab is selected')
        const fromaccount = page.getByLabel('From Account')
        await fromaccount.selectOption('2')
        const toaccount = page.getByLabel('To Account')
        await toaccount.selectOption('5')
        const amount = page.getByLabel('Amount')
        await amount.fill('500')
        const description = page.getByLabel('Description')
        await description.fill('Transfer money')
        await page.getByRole('button', { name: 'Continue' }).click()
        const tmmp_v = page.getByText('Please verify that the')
        await expect(tmmp_v).toBeVisible()
        const text = await tmmp_v.innerText()
        console.log('Verified message confirmation: ', text)
        await expect(fromaccount).toBeDisabled()
        await expect(toaccount).toBeDisabled()
        await expect(amount).toBeDisabled()
        await expect(description).toBeDisabled()
        await page.getByRole('button', { name: 'Submit' }).click()
        await expect(page.getByText('You successfully submitted')).toBeVisible()
        await page.getByText('username').click()
        await page.getByRole('link', { name: 'Logout' }).click()
        await expect(page.getByText('Signin')).toBeVisible()
        console.log('The account is actually logged out')
    });

    test('Test Case 2: Account Activity', async ({ page }) => {
        await page.goto('http://zero.webappsecurity.com/index.html')
        await page.getByText('Signin').click()
        await page.getByRole('textbox', { name: 'Login' }).fill('username')
        await page.getByRole('textbox', { name: 'Password' }).fill('password')
        await page.getByRole('button', { name: 'Sign in' }).click()
        await page.waitForLoadState("networkidle")
        await page.goto('http://zero.webappsecurity.com/bank/account-activity.html');
        const account_activity = page.locator('#account_activity_tab')
        await expect(account_activity).toHaveClass('active')
        await page.getByLabel('Account').selectOption('2')
        const checkings = [
            page.getByRole('cell', { name: 'CHECK DEPOSIT' }),
            page.getByRole('cell', { name: 'TELECOM' }),
            page.getByRole('cell', { name: 'CAR PAYMENT' })
        ]
        for (const checking of checkings) {
            await expect(checking).toBeVisible()
        }
        await page.getByText('username').click()
        await page.getByRole('link', { name: 'Logout' }).click()
        await expect(page.getByText('Signin')).toBeVisible()
        console.log('The account is actually logged out')
    });
});