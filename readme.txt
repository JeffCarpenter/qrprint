1. Download RedMon (http://pages.cs.wisc.edu/~ghost/redmon),
	extract it (to something like "c:\redmon") and run setup.exe for 32 bit Windows or setup64.exe for 64 bit
2. Open "Devices and Printers" (in Start Menu)
3. Create a "Redirected Port" (in the "Add Printer" screen)
4. Add a local printer using the redirected port (probably called RPT1).
	a) Use the Generic / Text Only driver.
	b) Name it "QR Code Creator"
5. Open the redirected port's properties
	- With the new printer selected, click "Print server properties"
	- Select RPT1 (or whatever you named it) and click "Configure Port"
6. Enter the full file path of "qr.bat"
7. Choose "Hidden" from the "Run" drop down