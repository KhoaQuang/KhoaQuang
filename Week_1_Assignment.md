# 📘 Week 1 Assignment – Playwright Foundations

## 🧪 Exercise 1: Practice Test Automation

**URL:** https://practicetestautomation.com/practice-test-login/  
**Spec file:** `practice.test.spec.ts`  
**Requirement:** Write **3 test cases** in the same spec file.

---

### ✅ Test Case 1: Positive Login Test

**Steps:**
1. Open the login page  
2. Enter username: `student`  
3. Enter password: `Password123`  
4. Click the **Submit** button  

**Assertions:**
- Verify the new page URL contains:  
  `practicetestautomation.com/logged-in-successfully/`
- Verify the page contains expected text:  
  `"Congratulations"` **or** `"successfully logged in"`
- Verify the **Log out** button is displayed  

---

### ❌ Test Case 2: Negative Username Test

**Steps:**
1. Open the login page  
2. Enter username: `incorrectUser`  
3. Enter password: `Password123`  
4. Click the **Submit** button  

**Assertions:**
- Verify the error message is displayed  
- Verify the error message text is:  
  `"Your username is invalid!"`  

---

### ❌ Test Case 3: Negative Password Test

**Steps:**
1. Open the login page  
2. Enter username: `student`  
3. Enter password: `incorrectPassword`  
4. Click the **Submit** button  

**Assertions:**
- Verify the error message is displayed  
- Verify the error message text is:  
  `"Your password is invalid!"`  

---

## 🏦 Exercise 2: Zero Bank Application

**Base URL:** http://zero.webappsecurity.com/index.html  
**Spec file:** `zero.bank.spec.ts`  
**Requirement:** Write **2 test cases** in the same spec file.

---

### 💸 Test Case 1: Transfer Funds

**Steps:**
1. Open the application  
2. Log in with credentials: `username / password`  
3. Navigate to:  
   `http://zero.webappsecurity.com/bank/transfer-funds.html`  
4. Click the **Transfer Funds** tab and verify it is selected  
5. Select **From Account:** `Checking (Avail. balance = $ -500.2)`  
6. Select **To Account:** `Credit Card (Avail. balance = $ -265)`  
7. Enter **Amount:** `500`  
8. Enter **Description:** `Transfer money`  
9. Click **Continue**  

**Assertions:**
- Verify confirmation message is displayed  
- Verify all fields are disabled  

**Final Steps:**
10. Click **Submit** and verify the transaction is successful  
11. Log out and verify the account is actually logged out  

---

### 📊 Test Case 2: Account Activity

**Steps:**
1. Open the application  
2. Log in with credentials: `username / password`  
3. Navigate to:  
   `http://zero.webappsecurity.com/bank/account-activity.html`  
4. Click the **Account Activity** tab and verify it is selected  
5. Select **Account:** `Checking`  

**Assertions:**
- Verify the returned table rows and content  

**Final Steps:**
6. Log out and verify the account is actually logged out  

---

## 🔧 Git Instructions

1. Create a new branch from `week1`  
2. Name your branch:
   ```
   week1_<yourname>
   ```
   Example: `week1_pttho`  

3. Implement your test cases  
4. Run tests locally and ensure all tests pass ✅  
5. Submit your project with the following rules:
   - Include all necessary source files  
   - **Exclude**:
     - `.github`
     - `node_modules`
     - `.gitignore`
     - `package-lock.json`

