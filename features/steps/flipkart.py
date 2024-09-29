from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


@given(u'I Launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

@when(u'Open Flipkart homepage')
def step_impl(context):
    context.driver.get("https://www.flipkart.com/")

sound_bar_button = None

@when(u'Click on Speakers and hover to soundbar')
def step_impl(context):
    action_chain = ActionChains(context.driver)

    context.driver.find_element(By.XPATH, "//span[text()='Electronics']").click()


    audio = context.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/object/a[1]")
    soundbar = context.driver.find_element(By.XPATH, "//a[text()='Soundbars']")

    context.sound_bar_button = action_chain.move_to_element(audio).move_to_element(soundbar)

@when(u'Click on soundbar')
def step_impl(context):
    context.sound_bar_button.click().perform()

@then(u'Click on price low to high')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                '//*[@id="container"]/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div[2]').click()

    time.sleep(1)

@then(u'items price must sort low to high')
def step_impl(context):
    product = context.driver.find_element(By.XPATH,
                                  '//*[@id="container"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/a[2]').text

    price = context.driver.find_element(By.XPATH,
                                '//*[@id="container"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/a[3]/div[1]/div[1]').text
    print(product, price)

    context.driver.close()
