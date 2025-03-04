from pywebpush import generate_vapid_keypair

private_key, public_key = generate_vapid_keypair()
print("VAPID_PUBLIC_KEY:", public_key)
print("VAPID_PRIVATE_KEY:", private_key)
