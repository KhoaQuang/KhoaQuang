import { Page } from '@playwright/test';
import { ENV } from '../utils/env';

export class LoginPage {
  constructor(private page: Page) {}

  get usernameInput() {
    return this.page.getByPlaceholder('Username');
  }

  get passwordInput() {
    return this.page.getByPlaceholder('Password');
  }

  get signInButton() {
    return this.page.locator('#loginForm\\:submitButton');
  }

  get logoutButton() {
    return this.page.locator('#logoutForm\\:log_out');
  }

  async goto() {
    await this.page.goto(ENV.baseUrl);
  }

  async login() {
    await this.usernameInput.fill(ENV.username);
    await this.passwordInput.fill(ENV.password);
    await this.signInButton.click();
  }

  async logout() {
    await this.logoutButton.click();
  }
}