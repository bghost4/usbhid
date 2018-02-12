import hid
import time

vendor_id = 0x0483
product_id = 0x5710

h = hid.device()
h.open(vendor_id, product_id) # TREZOR VendorID/ProductID

print("Manufacturer: %s" % h.get_manufacturer_string())
print("Product: %s" % h.get_product_string())
print("Serial No: %s" % h.get_serial_number_string())


for x in range(0,256):
    h.write([x])
    #time.sleep(1)
