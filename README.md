# RE-FLEX

Script for accepting work based on desired criteria, requires set up before use

As with anything PROCEED AT YOUR OWN RISK

'userdata' folder is dummy info, you'll need to get the info for header_data.py, json_data.py and registration_data.py through proxy (mitm, pcap, or charles proxy).

You can generate a dictionary for station names using runforstationlist.py, but only after initializing the script for the first time (since you will generate your 'user' and 'pw' file for your credentials. You may also make these files yourself and put the required info email in 'user' and password in 'pw' no extension, or just write it into the code itself in getAuth.py. Working to make stationlist generation more streamlined)

List of URLs to get from proxy for setup:

Device Info (not sure for iPhone):https://switchyard-na.amazon.com/distribution/app/AmazonFlexAndroidConfig

ServiceAreaId:https://flex-capacity-na.amazon.com/eligibleServiceAreas

Device Serial Number:https://odcs-na-extern.amazon.com/external/GetActiveDeviceForUserExternal

For header_data.py and json_data.py(if filters applied):https://flex-capacity-na.amazon.com/GetOffersForProviderPost

The two Device URLs are needed for registration data,

Device info has:

"device-type"

"os-version"

"device_model"

and Device Serial Number has:

device_serial

We were unable to find domain name but came to the conclusion it was the first item for "User-Agent" in Parenthesis, so in androids case, "Linux"
included is a script (once you have the 'user' and 'pw' files) that will generate your station list. Check for any utf-8 codes as those won't allow the script to work.

As of writing this, the script is working consistently.

Still under development
