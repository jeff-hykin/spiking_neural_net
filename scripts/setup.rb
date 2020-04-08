require 'atk_toolbox'

# mac os Sierra 10.12.6 (16G29)

if not OS.has_command('python')
    puts "you're going to need python3 to be installed (then retry this script)"
    exit 1
elsif Version.extract_from(`python --version`) < Version.new("3.6.0")
    puts "you're going to need to install python3.6 or higher (then retry this script)"
    exit 1
end

pip = "/usr/local/bin/python3 -m pip"

system "#{pip} install git+https://github.com/BindsNET/bindsnet.git" # version 
system "#{pip} install pybullet" # version 2.7.1

system "#{pip} install 'gym[all]'" # version 2.7.1
puts "=============================="
puts "="
puts "That^ will fail for the mujoco-py package, but thats to be expected. This project will run without it"
puts "="
puts "=============================="

puts "getting a specific version of opencv-python (3.4.5.20)".blue
system "#{pip} install opencv-python==3.4.5.20"
puts "\n\n\nif the above breaks, then check the avalible versions of opencv-python and install the closest one"