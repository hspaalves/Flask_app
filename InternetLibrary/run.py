from app import create_app

if __name__ == '__main__':
    env_name = 'development'
    print(env_name)
    app = create_app(env_name)
    app.run()
