import streamlit as st


def solution1():
    csharp_code = """
        
namespace HelloWorld
{
    class Program
    {
        public static void Main(string[] args)
        {
            string name = "Eli";
        }
    }
}    
               """
    st.code(csharp_code, language='csharp')


def solution2():
    csharp_code = """
        
namespace HelloWorld
{
    class Program
    {
        public static void Main(string[] args)
        {
            int num1 = 5;
            double num2 = 4.2;
            bool is_alive = true;
        }
    }
}


               """
    st.code(csharp_code, language='csharp')


def example1():
    csharp_code = """
        
namespace HelloWorld
{
    class Program
    {
        public static void Main(string[] args)
        {
            int age = 5;
            double num2 = 3.5;
            char singleCharacter = 'E';
            string name = "Eli";
            bool is_bigger = true;
            bool is_tried = false;
        }
    }
}
           """
    st.code(csharp_code, language='csharp')


def q1_steps():
    pass


def q1():
    csharp_code = """

    namespace HelloWorld
    {
        class Program
        {
            public static void Main(string[] args)
            {
                Console.WriteLine("Hello World!");
                string name = Console.ReadLine();

                Console.WriteLine("My name is "+name);
            }
        }
    }
        """
    st.code(csharp_code, language='csharp')


def q2():
    pass
