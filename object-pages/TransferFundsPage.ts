import {Page, expect} from '@playwright/test';
import { info } from 'node:console';

export class TransferFundsPage {
    readonly URL = 'http://zero.webappsecurity.com/bank/transfer-funds.html';
    constructor(private page:Page) {}
    get transferfundTab() {
        return this.page.locator('#transfer_funds_tab');
    }
    get fromaccountInput() {
        return this.page.getByLabel('From Account');
    }

    get toaccountInput() {
        return this.page.getByLabel('To Account');
    }

    get amountInput() {
        return this.page.getByLabel('Amount');
    }

    get descriptionInput() {
        return this.page.getByLabel('Description');
    }

    get continueButton() {
        return this.page.getByRole('button', { name: 'Continue' });
    }

    get submitButton() {
        return this.page.getByRole('button', { name: 'Submit' });
    }

    get verifyMessageConfirmation() {
        return this.page.getByText('Please verify that the');
    }

    get verifyTransactionSuccess() {
        return this.page.getByText('You successfully submitted');
    }

    async goto() {
        await this.page.goto(this.URL);
    }

    async verify_tranferfunds_active() {
        await expect(this.transferfundTab).toHaveClass('active')
        console.log('The Transfer Funds tab is selected')
    }

    async filltransferfunds(info: {
        fromaccount: string
        toaccount: string
        amount: string
        description: string
        }) {
        await this.fromaccountInput.selectOption(info.fromaccount)
        await this.toaccountInput.selectOption(info.toaccount)
        await this.amountInput.fill(info.amount)
        await this.descriptionInput.fill(info.description)
    }

    async continue_VerifyConfirmation() {        
        await this.continueButton.click()
        const tmmp_v = this.verifyMessageConfirmation
        await expect(tmmp_v).toBeVisible()
        const text = await tmmp_v.innerText()
        console.log('Verified message confirmation: ', text)
    }
    
    async verify_all_fields_disabled() {
        const fields = [
            this.fromaccountInput,
            this.toaccountInput,
            this.amountInput,
            this.descriptionInput
        ]
        for (const field of fields) {
            await expect(field).toBeDisabled()
        }
        await this.submitButton.click()
        await expect(this.verifyTransactionSuccess).toBeVisible()
    }
}