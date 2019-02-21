# List names of all available hardware
puts "Hardware available: "
foreach hardware_name [get_hardware_names] {
  puts $hardware_name
  if { [string match "DE*" $hardware_name] } {
      set usbblaster_name $hardware_name
  }
}

# List the names of all the devices attached to the system with the name "USB Blaster device"
puts "\nDevices on that hardware:"
foreach device_name [get_device_names -hardware_name $usbblaster_name] {
  puts $device_name
}


# Initiate a editing sequence
begin_memory_edit -hardware_name "DE-SoC \[USB-1\]" -device_name "@2: 5CSE(BA4|MA4)/5CSXFC4C6 (0x02D010DD)"

# Write memory content using the hex memory file
# update_content_to_memory_from_file -instance_index 0 -mem_file_path "memfile.hex" -mem_file_type hex
  
# Read memory content and save back to a hex memory file
save_content_from_memory_to_file -instance_index 0 -mem_file_path "memfile.hex" -mem_file_type hex

# End the editing sequence
end_memory_edit