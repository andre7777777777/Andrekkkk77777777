import requests
from bs4 import BeautifulSoup


def time():
    base_url = 'https://time.com/section/politics/'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'cookie': 'FastAB=0=2861,1=3771,2=6420,3=8633,4=4242,5=9574,6=0255,7=6705,8=5843,9=2137,10=0336,11=2902,12=1351,13=5408,14=4101,15=4581,16=0461,17=3387,18=9384,19=8501; stateCode=SPE; countryCode=RU; usprivacy=1---; optimizelyEndUserId=oeu1675524542679r0.4196034906444124; FastAB_Zion=5.1; AMCVS_7FF852E2556756057F000101%40AdobeOrg=1; seenBreakingNews=; s_ecid=MCMID%7C12340061808467867304094209336092263513; AMCV_7FF852E2556756057F000101%40AdobeOrg=-1124106680%7CMCIDTS%7C19393%7CMCMID%7C12340061808467867304094209336092263513%7CMCAAMLH-1676129349%7C6%7CMCAAMB-1676129349%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1675531750s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; s_cc=true; btIdentify=c9b7a055-5b3f-430b-eae2-207c81a9e4ed; _bts=3b71c203-b64d-4f48-b55e-f6e8f2871378; _pbjs_userid_consent_data=3524755945110770; sato=1; umto=1; __qca=P0-1973114982-1675524547737; _bti=%7B%22app_id%22%3A%22cnn%22%2C%22bsin%22%3A%22aWldUjXRSb1Tnqqn71lWyzBld9Xl38kTy4NsrOVtjMnDUaLnxEVAokHDXT1XdXpJsXh9OvMDNiKeaqNURwIcKg%3D%3D%22%2C%22is_identified%22%3Afalse%7D; ug=63de79c70d3edd0a3f851700158c2016; ugs=1; goiz=94c1487171f74673ab5b53bf6cd6598e; zwmc=1076260139960925080; ifyr=LBWOMAUB-17-I5LE; kfyn=B25201CA-18A8-45CC-BE07-C2C46494D21B; _li_dcdm_c=.cnn.com; _lc2_fpi=d7ea6f2d6e56--01gregqnwrtx93drxayrbarxt3; _pubcid=0f94e59a-e424-459d-8cde-ec2701de4794; _lr_retry_request=true; _lr_env_src_ats=false; pbjs-unifiedid=%7B%22TDID%22%3A%22b16a527e-94d7-4200-8ef0-970fb13d987b%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-01-04T15%3A29%3A23%22%7D; _cc_id=4c24a8d6e9d24a7164d4b919e632cd71; panoramaId_expiry=1676129363725; panoramaId=63e68e9efc1df5679a37866ce1f516d53938e67fa63c32dc960f8f759f7cbe0a; __li_idex_cache=%7B%7D; pbjs_li_nonid=%7B%7D; CNNtosAgreed=191222; bea4r=63de79fdc83680a3f851700158c2016; _cb=BMWNy_51DTRBtVpQi; OptanonControl=ccc=RU&csc=&cic=1&otvers=202211.2.0&pctm=2023-02-04T15%3A30%3A22.602Z&reg=global&ustcs=1---&vers=3.1.26; nexus-web-application-identifier=12db27e1-e9c8-4a3a-a2ea-b9fdfd39e855|1675525170051; _v__chartbeat3=H2IKF1zb9LBUhYLG; geoData=st petersburg|SPE|192242|RU|EU|300|broadband|59.870|30.370|643003; _sp_ses.f5fb=*; _cb_svref=https%3A%2F%2Fedition.cnn.com%2F; _chartbeat5=; bounceClientVisit340v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgKYAmAlguQPYB2AdAMa0OPUC2RA7tQE5ikQAGhC8YIMpRqsWTDsJDkUAfQDm1ZSmIoU0mADMAhmC0ilaiJu266B46ZBbVMANoBdAL5A; outbrain_cid_fetch=true; _t_tests=eyJyNG52amFmZHRpYklBIjp7ImNob3NlblZhcmlhbnQiOiJEIiwic3BlY2lmaWNMb2NhdGlvbiI6WyJEVVZKdGsiXX0sInNVV3pCYU9qWnhOcm4iOnsiY2hvc2VuVmFyaWFudCI6IkEiLCJzcGVjaWZpY0xvY2F0aW9uIjpbIkRORlZKNCJdfSwiSVVsUTI4b3VMUG1XQiI6eyJjaG9zZW5WYXJpYW50IjoiQiIsInNwZWNpZmljTG9jYXRpb24iOlsiQlMwbFNFIl19LCJXejJPTUw3ZG5TaEcxIjp7ImNob3NlblZhcmlhbnQiOiJBIiwic3BlY2lmaWNMb2NhdGlvbiI6WyJDdzRKRGciXX0sInFVanpVTDRkNzE4b1ciOnsiY2hvc2VuVmFyaWFudCI6IkMiLCJzcGVjaWZpY0xvY2F0aW9uIjpbIkRPSFVmNyJdfSwiclh1NlZUNjg2ZjZ0RCI6eyJjaG9zZW5WYXJpYW50IjoiQiIsInNwZWNpZmljTG9jYXRpb24iOlsiQlBWcV9EIl19LCJsaWZ0X2V4cCI6Im0ifQ==; OptanonAlertBoxClosed=2023-02-04T16:26:42.577Z; cnprevpage_pn=cnn%3Ain%3Aedition%3A%2F; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Feb+04+2023+19%3A26%3A44+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=13d6620b-4e6f-467e-85ac-1dc6327282c6&interactionCount=1&landingPath=NotLandingPage&groups=BG1826%3A1%2Creq%3A1%2Ctdc%3A1%2Cven%3A1%2Cad%3A1%2Csm%3A1%2Cai%3A1%2Csmv%3A1%2Cdid%3A1%2Cpcp%3A1%2Csav%3A1%2Cpfv%3A1%2Cpcd%3A1%2Cmcp%3A1%2Cadv%3A1%2Cbb%3A1%2Cdsa%3A1%2Cdlk%3A1%2Cmap%3A1%2Ccad%3A1%2Cpf%3A1%2Cpzv%3A1%2Cfc%3A1%2Csid%3A1%2Ctc%3A1%2Cpdd%3A1%2Cmra%3A1%2Cgld%3A1%2Cpad%3A1%2Cpap%3A1%2Ccos%3A1%2Csa%3A1%2Csec%3A1&AwaitingReconsent=false&geolocation=RU%3B; _chartbeat2=.1675524622025.1675528012063.1.D-QLazBq-npBiX82ADgU3RlBnOFXy.3; _sp_id.f5fb=3249ca6d-50d0-4a95-99cc-fad80dc9e0bb.1675524551.2.1675528021.1675525895.6ca4889d-df78-42bc-b6aa-fdf0267eaad6'
    }

    r = requests.get(base_url, headers=headers)

    with open('html.html', 'w', encoding='utf-8') as f:
        f.write(r.text)
        f.close()

    s = BeautifulSoup(r.text, 'html.parser')

    s = s.find('b-pw-1280')
    
    print(s)
    # soup = s.find_all('a')
    #
    # for i in soup:
    #     if 'ukraine' in i.get_text().lower() or 'ukrainian' in i.get_text().lower():
    #         print('https://time.com/section' + i['href'])
    #         r = requests.get('https://time.com/section' + i['href'], headers=headers)
    #         s = BeautifulSoup(r.text, 'html.parser')
    #
    #         s = s.find('main')
    #
    #         img = s.find('img')
    #
    #         if img:
    #             img = img['src']
    #
    #         print(img)


time()