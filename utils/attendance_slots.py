import requests
def attendanceSlots(mobileNumber):
    url = ""

    payload = {
        "FormID": "STAFFTASKLIST_V2",
        "UniqueID": "e4bb1b78-454b-4bbc-a297-bef04wf8f8b89",
        "MobileNumber": mobileNumber,
        "IMEI": "USSD",
        "CodeBase": "USSD",
        "DeviceName": "USSD",
        "City": "NAIROBI",
        "LanguageID": "en",
        "Country": "KENYA",
        "RegisteredCountry": "KENYA",
        "NetworkCountry": "ke",
        "CarrierName": "SAF FOR YOU",
        "RiderLL": "-1.2648023,36.7632444",
        "LatLong": "-1.2648023,36.7632444",             
        "SoftwareVersion": "USSD",
        "CorporateStaffTasks": {},
    }
    headers = {
        "Content-Type": "application/json",
    }
    try:
        response = requests.post(url, headers=headers, data=payload)
    except:
        pass
      #   return{"hasError":True, "message":"We are experiencing some issues.\nPlease try again later."}


    response = {
       "Status":"000",
       "Message":"Corporate Found",
       "BlockedApps":"fr.dvilleneuve.lockito;com.lexa.fakegps;com.vision.privgpslitf;com.latitudelongitude.gpscoordinates;maplocation.shira.com.maplocation;mobi.coolapps.locationsimulator;com.blackkara.mockation;com.garryzon.myloc;com.mps527.gnav.offline325;com.parallelaxiom.fyl;com.unofinity.traveler;com.yntmar.gps;fake.location;fakelivelocation;jimyu.locationmap;location.mock;locationchanger;Mock Locations;mocklocations;virtuallocation;virtualphonenavigation;com.route66.maps5;changemygps;exa.free.fg;fake;Fake GPS;fake.gps;fake_gps;fakegps;fakelocation;fly.gps;flygps;gps.fake;gps.joystick;gps.spoof;gps_fake;gpsanywhere;gpsemulator;gpsfake;gpsjoystick;gpslocation;gpsspoof;locationfake;locationmock;lockito;mapfake;mapwalker;Mock;mockgeo;mockgps;mocklation;mockloc;mockme;movegps;com.vision.privgpslite;abubakarwangila92@gmail.com",
       "AllowedCheckins":[
          {
             "BranchID":"9B46CC6A",
             "BranchName":"Little HQ",
             "LatLong":"-1.2648256039106576,36.763340397508514"
          }
       ],
       "Corporates":[
          {
             "CorporateID":"0A2B34D2",
             "BranchID":"Little",
             "BranchName":"Little HQ",
             "DepartmentID":"D8A84BF4",
             "DepartmentName":"Tech Team",
             "LatLong":"-1.2648256039106576,36.763340397508514",
             "VarianceInMeters":200,
             "Tasks":[
                {
                   "QRCode":True,
                   "TaskID":"75D0564B",
                   "TaskDateTime":"09:37",
                   "TimeFlag":"0",
                   "TaskName":"Arrived at Work",
                   "PrerequisiteTasks":"",
                   "RecommendedTime":"08:00"
                },
                {
                   "QRCode":True,
                   "TaskID":"59495B25",
                   "TimeFlag":"0",
                   "TaskName":"Out for Lunch",
                   "PrerequisiteTasks":"75D0564B",
                   "RecommendedTime":"13:00"
                },
                {
                   "QRCode":True,
                   "TaskID":"C73BAFD6",
                   "TimeFlag":"0",
                   "TaskName":"Back From Lunch",
                   "PrerequisiteTasks":"59495B25",
                   "RecommendedTime":"14:00"
                },
                {
                   "QRCode":True,
                   "TaskID":"F623E512",
                   "TimeFlag":"0",
                   "TaskName":"Leaving Work",
                   "PrerequisiteTasks":"75D0564B",
                   "RecommendedTime":"17:00"
                }
             ]
          }
       ],
       "CurrentTime":"11:21"
    }

    return response



