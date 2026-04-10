import {Page, expect} from '@playwright/test';

export class AccountActivityPage {
    readonly URL = 'http://zero.webappsecurity.com/bank/account-activity.html';
    constructor(private page:Page) {}
    get accountactivityTab() {
        return this.page.locator('#account_activity_tab');
    }
    get accountInput() {
        return this.page.getByLabel('Account');
    }

    get continueButton() {
        return this.page.getByRole('button', { name: 'Continue' });
    }

    get submitButton() {
        return this.page.getByRole('button', { name: 'Submit' });
    }

    get checkdeposit() {
        return this.page.getByRole('cell', { name: 'CHECK DEPOSIT' });
    }

    get telecom() {
        return this.page.getByRole('cell', { name: 'TELECOM' });
    }

    get carpayment() {
        return this.page.getByRole('cell', { name: 'CAR PAYMENT' });
    }

    async goto() {
        await this.page.goto(this.URL);
    }

    async account_activity_tab(info: {
        checkstatus: string,
        account: string
        }) {
        await expect(this.accountactivityTab).toHaveClass(info.checkstatus)
        await this.accountInput.selectOption(info.account)
        const checkings = [
            this.checkdeposit,
            this.telecom,
            this.carpayment
        ]
        for (const checking of checkings) {
        await expect(checking).toBeVisible()
        }
    }
}