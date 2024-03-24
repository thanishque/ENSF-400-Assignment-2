import ansible_runner

def run_playbook():
    r = ansible_runner.run(private_data_dir='.', inventory='hosts.yml', playbook='hello.yml')

    print("Playbook Results:")
    for result in r.events:
        print(result)

if __name__ == "__main__":
    run_playbook()
