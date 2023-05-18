#--- Import Library
print("Importing the libraries.....")
from dtwinpylib.dtwinpy.Digital_Twin import Digital_Twin
factory_ip = "192.168.0.50"
my_ip = "127.0.0.1"

#--- Create a Digital Twin object with the require inputs
mydt = Digital_Twin(
    name= "5s_determ",
    template= True, 
    Freq_Sync= 2, 
    Freq_Valid= 30, 
    Freq_Service= 2, 
    delta_t_treshold=5,
    ip_address=factory_ip,
    flag_API= True,
    rct_threshold= 0,
    rct_queue= 2,
    flag_external_service= True,
    logic_threshold= 0.000,
    input_threshold=0.000)

#--- Run the real time Digital Twin
mydt.run()
