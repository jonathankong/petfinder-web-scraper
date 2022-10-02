import base64
import win32com.client as win32

def send_outlook_email(path, catNames, catLinkList, catImgs):

    encoded_image = base64.b64encode(open(f'{path}\{catNames[0]}.png', "rb").read()).decode("utf-8")

    outlook = win32.Dispatch('outlook.application')

    mail = outlook.CreateItem(0)
    mail.Subject = 'Testing Email'
    mail.BodyFormat= 2
    mail.Body = 'Hello World'
    mail.To = 'icesnowwaterme@gmail.com'
    mail.HTMLBody = f"""
        <h1><a href="{catLinkList[0]}">{catNames[0]}</a></h1>
        {catImgs[0].get_attribute('outerHTML')}
    """
    
    # mail.HTMLBody = f"""
    #     <h1><a href="{catLinkList[0]}">{catNames[0]}</a></h1>
    #     <img src="data:image/png;base64,{encoded_image}"/>
    # """
    mail.Display()
    #mail.Send()
