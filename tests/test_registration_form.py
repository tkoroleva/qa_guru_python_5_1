from selene import have
from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys


def test_registration_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    browser.element('#firstName').type('Dana')
    browser.element('#lastName').type('Scully')
    browser.element('#userEmail').type('scully@fbi.gov')

    browser.all('[for^=gender-radio-2]').element_by(have.text('Female')).click()
    browser.element('#userNumber').type('5551013000')

    browser.element('#dateOfBirthInput').click().type(Keys.CONTROL+'a'+Keys.NULL+'23 Feb 1964')

    browser.element('#subjectsInput').type('Physics').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()

    browser.element('#currentAddress').type('Maryland, Annapolis')
    browser.element('#react-select-3-input').type('Rajasthan').press_enter()
    browser.element('#react-select-4-input').type('Jaiselmer').press_enter()
    browser.element('#submit').press_enter()

    browser.element('[class^=modal-title]').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.exact_texts(
        'Dana Scully',
        'scully@fbi.gov',
        'Female',
        '5551013000',
        '23 February,1964',
        'Physics',
        'Reading',
        '',
        'Maryland, Annapolis',
        'Rajasthan Jaiselmer'
    )
    )
