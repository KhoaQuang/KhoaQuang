import {Page, expect} from '@playwright/test';

export class HomePage {
    constructor(private page:Page) {}
    get logoutButton() {
        return this.page.getByText('Log out');
    }

    get expectedtext() {
        return this.page.getByText('Congratulations');
    }

    get error_invalid() {
        return this.page.locator('#error');
    }

    async expected_text() {
        await expect(this.expectedtext).toBeVisible()
        const text = await this.expectedtext.innerText()
        console.log('Expected text: ', text)
        await expect(this.logoutButton).toBeVisible()
    }

    async verify_message_invalid() {
        await expect(this.error_invalid).toBeVisible()
        const text = await this.error_invalid.innerText()
        console.log('The error message text is: ', text)
    }
}