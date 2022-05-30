from pom.home_view import home_view

def test_search(driver):
    baseurl = ('https://www.tickertape.in/')
    driver.get(baseurl)

    home_obj = home_view(driver)
    home_obj.search_stock()
    home_obj.click_res()