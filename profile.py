import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.igext as IG

pc = portal.Context()
request = pc.makeRequestRSpec()

node = request.XenVM("docker")
node.cores = 4
node.ram = 4096
node.routable_control_ip = "true" 

bs_landing = node.Blockstore("bs_image", "/image")
bs_landing.size = "500GB"
  
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
node.routable_control_ip = "true"
node.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/install_docker.sh"))
node.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/"))

pc.printRequestRSpec(request)
