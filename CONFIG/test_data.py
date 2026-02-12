TEST_DATA = {

    # ------------------------------------------------------------------
    # ROLES (mapping logic-level names to user keys)
    # ------------------------------------------------------------------
    "roles": {
        "OWNER": "A",
        "USER": "B"
    },

    # ------------------------------------------------------------------
    # BROWSERS (centralized, reusable)
    # ------------------------------------------------------------------
    "browsers": {
        "chrome": "chrome",
        "edge": "edge",
        "firefox": "firefox"
    },

    # ------------------------------------------------------------------
    # COMMON CLIENT CONFIG
    # ------------------------------------------------------------------
    "client": {
        "host": "10.128.224.115",
        "screenshot_dir": "../Screenshots"
    },

    # ------------------------------------------------------------------
    # IVIEW CONFIG
    # ------------------------------------------------------------------
    "iview": {
        "url": "https://10.103.3.173/iview/views/index.jsf",
        "username": "admin",
        "password": "AvayaMcspv_1234$"
    },

    # ------------------------------------------------------------------
    # PORTAL CONFIG (shared address)
    # ------------------------------------------------------------------
    "portal": {
        "url": "https://aawgott-svc-kvm.hcm.com/portal/tenants/default/"
    },

    # ------------------------------------------------------------------
    # USERS (MULTI-USER CORE)
    # ------------------------------------------------------------------
    "users": {
        "A": {
            "portal_username": "khoa",
            "portal_password": "AvayaMcspv_1234$",
            "role": "owner",
            "browser": "chrome"
        },
        "B": {
            "portal_username": "khoa2",
            "portal_password": "RAPtor1234",
            "role": "participant",
            "browser": "chrome"
        }
    },

    # ------------------------------------------------------------------
    # MEETING DATA
    # ------------------------------------------------------------------
    "meeting": {
        "id": "4602112",
        "topic": "Automation Test Meeting"
    }
}
