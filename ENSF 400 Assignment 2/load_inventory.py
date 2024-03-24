import ansible_runner

def load_inventory_and_ping():
    r = ansible_runner.run(private_data_dir='.', inventory='hosts.yml', playbook='ping.yml')
    
    print("Hosts information:")
    for host in r.inventory.hosts.values():
        print(f"Name: {host.name}, IP Address: {host.vars['ansible_host']}, Groups: {', '.join(host.groups)}")

    print("\nPing Results:")
    for host, result in r.events['runner_on_ok'].items():
        print(f"{host}: {result['ping']}")

if __name__ == "__main__":
    load_inventory_and_ping()
