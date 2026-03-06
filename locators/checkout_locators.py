class CheckoutStepOneLocators:
    FIRST_NAME = "[data-test='firstName']"
    LAST_NAME = "[data-test='lastName']"
    POSTAL_CODE = "[data-test='postalCode']"
    CONTINUE_BUTTON = "[data-test='continue']"


class CheckoutStepTwoLocators:
    SUMMARY_CONTAINER = ".summary_info"
    ITEM_NAMES = ".inventory_item_name"
    ITEM_TOTAL = ".summary_subtotal_label"
    TAX = ".summary_tax_label"
    TOTAL = ".summary_total_label"
    FINISH_BUTTON = "[data-test='finish']"
    CANCEL_BUTTON = "[data-test='cancel']"


class CheckoutCompleteLocators:
    COMPLETE_CONTAINER = "#checkout_complete_container"
    TITLE = "[data-test='complete-header']"
    MESSAGE = "[data-test='complete-text']"
    COMPLETE_HEADER = ".complete-header"
    COMPLETE_TEXT = ".complete-text"
