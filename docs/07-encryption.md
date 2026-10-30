# 7. Encryption: where I would start

I wanted to go beyond saying "encrypt your data" and actually document what that means for this setup.

There are two separate problems: protecting files on the drive, and protecting traffic between computers. I'm treating them separately.

## Encryption at rest

For a dedicated Linux machine, I would use LUKS2 on a separate data volume. **This example destroys everything on the selected partition. Do not run it against an existing drive or your main system disk.** Back up and verify the backup first.

Find the correct disk and partition:

```bash
lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS
```

On a NEW, EMPTY test partition only, replace the placeholder after verifying it:

```bash
sudo cryptsetup luksFormat /dev/REPLACE_WITH_EMPTY_PARTITION
sudo cryptsetup open /dev/REPLACE_WITH_EMPTY_PARTITION llm_data
sudo mkfs.ext4 /dev/mapper/llm_data
sudo mkdir -p /srv/llm-data
sudo mount /dev/mapper/llm_data /srv/llm-data
sudo cryptsetup status llm_data
```

A successful status check tells me the mapped device is encrypted. It does not tell me whether every application file is stored there.

Before changing Docker storage, I would confirm where Ollama writes its model data and map that storage to the encrypted volume. The Compose example in the root of this repository still uses a regular Docker volume, so it **does not** implement this step yet.

Important: LUKS protects data when the encrypted volume is locked. It does not stop a process with sufficient access from reading data while the volume is mounted. I would also plan how the unlock key is stored, how recovery works, and what happens after a reboot.

## Encryption in transit

For local testing, the API binds to 127.0.0.1. That means I can reach it from the host without publishing it to the network.

If I later need access from another computer, I would put an authenticated TLS reverse proxy in front of it rather than exposing the Ollama port directly.

Check the current binding:

```bash
docker compose port ollama 11434
```

For a remote deployment, I would verify the certificate and TLS connection with:

```bash
curl --fail --verbose https://YOUR_INTERNAL_LLM_HOST/api/version
```

This command is a future verification example. It will not work until a valid HTTPS endpoint and authentication setup exist. I would never use `curl -k` as proof that certificate validation is working.

## What I would test

- Can the encrypted data volume be unlocked and mounted after a restart?
- Are the actual model files and application data on the encrypted volume?
- Are backups encrypted separately?
- Does the HTTPS endpoint reject invalid certificates?
- Can someone bypass the proxy and reach the Ollama API directly?

Next: [authentication and access](08-access-and-auditing.md).
