echo "WARNING! Your ip CAN get blacklisted on databases such as 'abuseipdb.com'. You have been warned."
sleep 5
mkdir out
echo "press ctrl + c when you feel you have enough hosts."
sudo masscan -p 80,443 --open 0.0.0.0-255.255.255.255 --exclude 0.0.0.0 -oX web.txt --rate 1000
python3 extract.py > filtered.txt
mv web.txt out/
python3 mkhtml.py > index.html
mv filtered.txt out/
mv index.html out/
mv paused.conf out/
echo "You will find 'index.html' in the 'out/' directory. This allows easy access to the scanned ips."
