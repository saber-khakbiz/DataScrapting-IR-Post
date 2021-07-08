from stdiomask import getpass
from cowsay import daemon, ghostbusters, kitty
from check_validation_ID_Post import check_validation
from driver_chrome import *
from DataScrapting import *

tracking_ID = getpass("Enter Your Post Id(24 digit): ")
check_validation(tracking_ID)


URL = f"https://tracking.post.ir/?id={tracking_ID}&client=app"
driver = driverChomre(URL)

kitty("\nplease wait...\n")

page_source = PageSource(driver)

soup = mining(page_source)
warning = soup.warning()
security = soup.security()


if warning == None and security == None :
    dst_lst = soup.FindAll()
    new_lst = [(i.text, j.text) for i,j in zip(
                                    [i for i in dst_lst if not dst_lst.index(i)%2],
                                    [i for i in dst_lst if dst_lst.index(i)%2]
                                    )
    ]
    new_lst.reverse()
    print("\n*******************************************************************")
    for i,dst in enumerate(new_lst):
        print(f"\t\t\t{i+1}\n")
        print(f"{dst[0]}\n")
        print(f"{dst[1]}")
        print("========================================================================")

elif warning != None :
    ghostbusters(f"\n {warning.text}")

else:
    daemon("از سمت شما ترافیک بالایی سمت سرویس های ما ارسال می شود!")