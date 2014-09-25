VM_MEMORY = "1024"
VM_NAME = "ng"

Vagrant.require_version ">=1.6.0"
Vagrant.configure("2") do |config|
    config.vm.hostname = "ng"
    config.vm.network :forwarded_port, guest: 80, host: 8080, auto_correct:true # nginx
    config.vm.network :forwarded_port, guest: 5432, host: 5432, auto_correct:true # postgres
    config.vm.network :forwarded_port, guest: 6379, host: 6379, auto_correct:true # redis
	config.vm.network :forwarded_port, guest: 8000, host: 8000, auto_correct:true # django
	config.vm.network :forwarded_port, guest: 9001, host: 9001, auto_correct:true # supervisor
	config.vm.network :forwarded_port, guest: 9200, host: 9200, auto_correct:true # elasticsearch

    if Vagrant.has_plugin?("vagrant-cachier")
        config.cache.scope = :box
    end

	config.vm.define "local" do |local|		
		local.vm.provider "virtualbox" do |provider, override|
			provider.name = VM_NAME
			provider.gui = false
			provider.customize ["modifyvm", :id, "--memory", VM_MEMORY]
        	provider.customize ["modifyvm", :id, "--cpuexecutioncap", "100"]
			provider.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/v-root", "1"]
			provider.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        	provider.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
            override.vm.box = "ubuntu/trusty64"
			override.vm.box_url = "https://vagrantcloud.com/ubuntu/trusty64"
        	override.vm.network "private_network", ip: "192.168.100.10"
		end
	end

	config.vm.provision :ansible do |ansible|
		ansible.playbook = "provisioning/playbook.yml"
		ansible.inventory_path = "provisioning/hosts-vagrant"
		ansible.verbose = 'v'
		ansible.extra_vars = { ansible_ssh_user: 'vagrant' }
		ansible.limit = 'all'
	end

end
