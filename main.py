from roboid import *
import keyboard

def main():
    # 기본형 햄스터 로봇 객체 생성 (docs 기반)
    hamster = Hamster()
    print("docs 폴더의 8차시 예제를 기반으로 키보드 제어 코드를 시작합니다.")
    print("------------------------------------------")
    print("  [조작 방법]")
    print("  - 위 방향키 (▲) : 전진 (최대 속도 100)")
    print("  - 아래 방향키 (▼) : 후진 (최대 속도 -100)")
    print("  - 왼쪽 방향키 (◀) : 제자리 좌회전 (속도 100)")
    print("  - 오른쪽 방향키 (▶) : 제자리 우회전 (속도 100)")
    print("  - 스페이스바 (Space) : 정지")
    print("------------------------------------------")
    print("종료하려면 Ctrl+C를 누르세요.")
    
    try:
        while True:
            # Keyboard.read()와 keyboard.is_pressed() 조합 사용
            key = Keyboard.read()  # 키보드 이벤트를 얻는다.
            
            # 속도값을 최대값인 100으로 설정하여 아주 빠르게 이동하도록 수정했습니다.
            if keyboard.is_pressed("up"):      # 위 방향키를 눌렀을 경우
                hamster.wheels(100)
            elif keyboard.is_pressed("down"):    # 아래 방향키를 눌렀을 경우
                hamster.wheels(-100)
            elif keyboard.is_pressed("right"):   # 오른쪽 방향키를 눌렀을 경우
                hamster.wheels(100, -100)
            elif keyboard.is_pressed("left"):    # 왼쪽 방향키를 눌렀을 경우
                hamster.wheels(-100, 100)
            elif keyboard.is_pressed(" "):       # 스페이스 바를 눌렀을 경우
                hamster.wheels(0)
                
            wait(20)  # 너무 빨리 반복하지 않도록 한다.
            
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다. 로봇을 정지합니다.")
        hamster.wheels(0, 0)

if __name__ == "__main__":
    main()
