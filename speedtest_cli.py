import speedtest
import time

st = speedtest.Speedtest()

print("The speed test will give the result in a few seconds")
while True:
    # I am speedtest, hello!
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping

    #printer
    print(f"Download: {download_speed:.2f} Mbps")
    print(f"Upload: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")
    
    #Please don't go
    command = input("Enter command (exit , sp for restart): ").strip().lower()
    
    #"thank you"
    if command == "exit":
        print("Exit...")
        break

    #thank you
    elif command == "sp":
        print("Restart speed test...")
        continue
    
    #unknown lol
    else:
        print("Unknown command. Go ahead...")
        
    time.sleep(5)
