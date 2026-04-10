import { test, expect } from '@playwright/test';
import { LoginFormPage } from '../object-pages/LoginFormPage';
import { TransferFundsPage } from '../object-pages/TransferFundsPage';
import { AccountActivityPage } from '../object-pages/AccountActivityPage';
import { TopHeaderPage } from '../object-pages/TopHeaderPage';

const info = {
    username: 'username', 
    password: 'password'
}

const info_tf = {
    fromaccount: '2',
    toaccount: '5',
    amount: '500',
    description: 'Transfer money'
}

const info_aa = {
    checkstatus: 'active',
    account: '2'
}

test.describe('Exercise 2: Zero Bank Application', () => {
    let loginFormPage: LoginFormPage, transferFundsPage: TransferFundsPage, accountActivityPage: AccountActivityPage, topHeaderPage: TopHeaderPage;
    test.beforeEach(async({ page }) => {
        loginFormPage = new LoginFormPage(page)
        transferFundsPage = new TransferFundsPage(page)
        accountActivityPage = new AccountActivityPage(page)
        topHeaderPage = new TopHeaderPage(page)
        await loginFormPage.goto()
        await loginFormPage.login(info.username, info.password)
    });

    test('Test Case 1: Transfer Funds', async ({ page }) => {
        await page.waitForTimeout(3000)
        await transferFundsPage.goto()
        await transferFundsPage.verify_tranferfunds_active()
        await transferFundsPage.filltransferfunds(info_tf)
        await transferFundsPage.continue_VerifyConfirmation()
        await transferFundsPage.verify_all_fields_disabled()
        await topHeaderPage.verify_loggedOut()
    });

    test('Test Case 2: Account Activity', async ({ }) => {
        await accountActivityPage.goto();
        await accountActivityPage.account_activity_tab(info_aa)
        await topHeaderPage.verify_loggedOut()
    });
});