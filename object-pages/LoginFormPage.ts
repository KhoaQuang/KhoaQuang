import {Page, expect} from '@playwright/test';

export class LoginFormPage {
    readonly URL = 'http://zero.webappsecurity.com/index.html';
    constructor(private page:Page) {}
    get signinButton() {
        return this.page.getByText('Signin');
    }
    get usernameInput() {
        return this.page.getByRole('textbox', { name: 'Login' });
    }

    get passwordInput() {
        return this.page.getByRole('textbox', { name: 'Password' });
    }

    get signInButton() {
        return this.page.getByRole('button', { name: 'Sign in' });
    }
    
    async goto() {
        await this.page.goto(this.URL);
    }

    async login(username:string , password:string) {
        await this.signinButton.click();
        await this.usernameInput.fill(username);
        await this.passwordInput.fill(password);
        await this.signInButton.click();
        await this.page.waitForLoadState("networkidle")
    }

    async verify_URL() {
        await expect(this.page).toHaveURL(/logged-in-successfully/)
    }
}