class Locators:
    ##########################LoginPage.py############################

    indexEmail_id = 'index_email'
    indexPassword_id = 'index_pass'
    signinButton_id = 'index_login_button'
    topProfileMenu_css = '.TopNavBtn__profileArrow > svg'
    topLogoutButton_xpath = '//*[@id="top_logout_link"]/span'
    topHomeLink_small_css = '.TopHomeLink path:nth-child(2)'
    topHomeLink_big_css = '.TopHomeLink > svg'

    ##########################ChangeUserInfo.py############################

    mainPage_id = 'l_pr'
    profileEdit_id = 'profile_edit_act'
    fsField_css = '#container2 .selector_input'
    fsDating_id = 'option_list_options_container_2_3'
    bdField_css = '#container4 .selector_input'
    bd5_id = 'option_list_options_container_4_5'
    bmField_css = '#container5 .selector_input'
    bmMarch_id = 'option_list_options_container_5_3'
    byField_css = '#container6 .selector_input'
    by1990_id = 'option_list_options_container_6_19'
    ruLanguage_id = 'bit_8_0'
    azLanguage_id = 'bit_8_57'
    delRusLang_id = '//*[@id="bit_8_0"]/span[2]/span[1]'
    delAzLang_id = '//*[@id="bit_8_57"]/span[2]/span[1]'
    langField_css = '#container8 .selector_input'
    addAzLang_xpath = "//li[@title='Azərbaycan dili Азербайджанский']"
    bSaveProfInfo = "//*[@id='pedit_general']/div[17]/button"
