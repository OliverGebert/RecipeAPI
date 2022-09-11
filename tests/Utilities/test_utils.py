from Utilities import check_password, hash_password


def test_hash_password():
    """hash_password should return a 265bit SHA hash value"""
    hash_recipe = hash_password("Recipe")
    hash_user = hash_password("User")

    assert "$pbkdf2-sha256" in str(hash_recipe)  # assert value is SHA256 hash
    assert "$pbkdf2-sha256" in str(hash_user)  # assert value is SHA265 hash
    assert hash_recipe != hash_user  # assert two hash values differ


def test_check_password():
    """confirm that hash of a given string is correct"""
    pwd = "mypassword"
    hash = hash_password(pwd)

    assert check_password("otherpwd", hash) == False
    assert check_password(pwd, hash)
