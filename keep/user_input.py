import streamlit as st

def user_input1():
    st.subheader("דוגמא ראשונה ")
    csharp_code = """

    
namespace HelloWorld
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter your name : ");
            string name = Console.ReadLine();
            Console.WriteLine("Your name is "+name);
        }
    }
}

                                   """
    st.code(csharp_code, language='csharp')

def casting():

    csharp_code = """

namespace HelloWorld
{
    class Program
    {
        public static void Main(string[] args)
        {
            string numString = "42";
            Console.WriteLine(numString.GetType());
            int num = int.Parse(numString);
            Console.WriteLine(num.GetType());
        }
    }
}





                                       """
    st.code(csharp_code, language='csharp')
