1. Download RedMon from http://pages.cs.wisc.edu/~ghost/redmon,
2. Install RedMon
	a) Extract it (to something like "c:\redmon")
	b) Run setup.exe for 32 bit Windows or setup64.exe for 64 bit
3. Open "Devices and Printers" (in Start Menu)
4. Create a "Redirected Port" (in the "Add Printer" screen)
5. Add a local printer using the redirected port (probably called RPT1).
	a) Use the Generic / Text Only driver.
	b) Name it "QR Code Creator"
6. Open the redirected port's properties
	a) With the new printer selected, click "Print server properties"
	b) Select RPT1 (or whatever you named it) and click "Configure Port"
7. Enter the full file path of "qr.bat"
8. Choose "Hidden" from the "Run" drop down