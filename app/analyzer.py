from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)
    return {
        'password': password,
        'score': result['score'],
        'crack_time': result['crack_times_display']['offline_slow_hashing_1e4_per_second'],
        'feedback': result['feedback']
    }
