# �u���E�U���J���B
driver = webdriver.Chrome()

# Google�̌���TOP��ʂ��J���B
driver.get("https://www.google.co.jp/")

# ������Ƃ��āuselenium�v�Ɠ��͂��AEnter�L�[�������B
driver.find_element_by_id("lst-ib").send_keys("selenium")
driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)

# �^�C�g���ɁuSelenium - Web Browser Automation�v�ƈ�v���郊���N���N���b�N����B
driver.find_element_by_link_text("Selenium - Web Browser Automation").click()

# �u���E�U���I������B
driver.close()
