import sys
import json
import nose

from selenium import webdriver


sauce_url = "http://{user}:{key}@ondemand.saucelabs.com:80/wd/hub"
test_config = json.load(open("test_config.json"))


def run_browser(browser_info):
    d = webdriver.Remote(
        desired_capabilities=browser_info,
        command_executor=sauce_url.format(**test_config)
    )
    d.implicitly_wait(30)
    d.get(test_config["url"])
    d.switch_to_frame("ad_child")
    try:
        assert d.find_element_by_tag_name("body").text == "child"
    finally:
        print("Link to your job: https://saucelabs.com/jobs/%s" % d.session_id)
        d.quit()


def test_browsers():
    browsers = [
        ("INTERNETEXPLORER", "6", "Windows 2003"),
        ("INTERNETEXPLORER", "7", "Windows 2003"),
        ("INTERNETEXPLORER", "8", "Windows 2003"),
        ("INTERNETEXPLORER", "9", "Windows 2008"),
        ("INTERNETEXPLORER", "10", "Windows 2012"),
        ("FIREFOX", "3.0", "Windows 2012"),
        ("FIREFOX", "4", "Windows 2012"),
        ("FIREFOX", "17", "Windows 2003"),
        ("CHROME", "", "Windows 2003"),
        ("OPERA", "11", "Windows 2003"),
        ("OPERA", "12", "Windows 2003"),
        ({"browserName": "safari"}, "5", "Windows 2008"),
        ({"browserName": "ipad"}, "4.3", "Mac 10.6"),
        ({"browserName": "ipad"}, "6", "Mac 10.8"),
        ("IPHONE", "4.3", "Mac 10.6"),
        ("IPHONE", "6", "Mac 10.8"),
        ("ANDROID", "4", "Linux"),
    ]
    for name, version, platform in browsers:
        if type(name) is str:
            browser_info = getattr(webdriver.DesiredCapabilities, name).copy()
        else:
            browser_info = name
        browser_info.update(version=version, platform=platform, name="adsandbox")
        yield run_browser, browser_info


if __name__ == "__main__":
    nose.core.run(argv=["nosetests", "-vv", __file__])
