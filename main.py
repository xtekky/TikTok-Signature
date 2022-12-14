from signer.main import Signer

with Signer() as signer:
    verify_fp, signature, device_id, tt_params = signer._sign('https://us.tiktok.com/api/commit/follow/user/?aid=1988&app_language=zh-Hant-TW&app_name=tiktok_web&battery_info=0.58&browser_language=zh-CN&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F97.0.4692.99%20Safari%2F537.36&channel=tiktok_web&channel_id=0&cookie_enabled=true&device_id=7044877592931976705&device_platform=web_pc&focus_state=true&from=18&fromWeb=1&from_page=user&from_pre=0&history_len=2&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=&referer=&region=US&screen_height=900&screen_width=1440&sec_user_id=MS4wLjABAAAAYQIn0ghGQeUMmuqngrxATRDvKvq8dksgQBjXfrOdFo6wdO3DGbciDey2TfJE6EAR&type=1&tz_name=America%2FChicago&user_id=7035930273985479685&webcast_language=zh-Hant-TW&msToken=9ZVRfvLh5KCA9fRwcMTx5ysMVMj7H45hx2NXcHnbY9e1jcESeY2W74Pg3yyBDNFWV8FiPTkZKizt9BhfdgLhahVygTko7rZsISzU8zN408oycsxLlALrDRHd5mW-jBPFsda-dQ==&X-Bogus=DFSzs3fLzhXANxVYSLIiPRKeej0y&_signature=_02B4Z6wo00001j7htJQAAIDDQG3qaCLmgBY-4dgAAO5X40')
    print(signature)
    print(device_id)
    print(verify_fp)
    print(tt_params)

        # # Prints the author's username of the trending video.
        # print(trending_video.author.username)