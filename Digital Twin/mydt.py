#--- Import Library
print("Importing the libraries.....")
from dtwinpylib.dtwinpy.Digital_Twin import Digital_Twin
from dtwinpylib.dtwinpy.tester import Tester


factory_ip = "192.168.0.50"
home_ip = "127.0.0.1"

my_ip = factory_ip



#--- create test object and replace the initial.json in the models folder
test = Tester()
test.initiate()

#--- Create a Digital Twin object with the require inputs
mydt = Digital_Twin(
    name= test.name,
    template= True, 
    Freq_Sync= test.Freq_Sync, 
    Freq_Valid= test.Freq_Valid, 
    Freq_Service= test.Freq_Service, 
    delta_t_treshold= test.delta_t_treshold,
    ip_address=my_ip,
    flag_API= test.flag_API,
    rct_threshold= test.rct_threshold,
    rct_queue= test.rct_queue,
    flag_external_service= test.flag_external_service,
    flag_publish = test.flag_publish,
    logic_threshold= test.logic_threshold,
    input_threshold= test.input_threshold,
    flag_validation=test.flag_validation)

mydt.run()
