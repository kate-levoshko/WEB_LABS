using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    public delegate int Calculate(int x, int y);

    public class ActiveClass
    {
        public event Calculate StartCalculation;

        public void TryToCalc(int x, int y)
        {
            StartCalculation?.Invoke(x, y);
        }
    }

    public class PassiveClass
    {
        public int Add(int x, int y) { Console.WriteLine("{0} + {1} = {2}", x, y, x+y); return x + y; }
        public int Sub(int x, int y) { Console.WriteLine("{0} - {1} = {2}", x, y, x - y); return x - y; }
    }

    public class Product
    {
        public decimal Price { get; set; }
    }

    public static class MyExtension
    {
        public static decimal Discount(this Product product)
        {
            return product.Price * .9M;
        }
    }

    class Program
    {
        static void Main11(string[] args)
        {
            #region Classical events and handlers
            /* ActiveClass activeObj = new ActiveClass();
             PassiveClass passiveObj = new PassiveClass();

             activeObj.StartCalculation += passiveObj.Add;
             activeObj.StartCalculation += passiveObj.Sub;

             activeObj.TryToCalc(5, 4);*/
            #endregion

            #region anonimous methods
            /*ActiveClass a = new ActiveClass();
            a.StartCalculation += delegate (int x, int y) { Console.WriteLine("{0} + {1} = {2}", x, y, x + y); return x + y; };
            a.StartCalculation += delegate (int x, int y) { Console.WriteLine("{0} - {1} = {2}", x, y, x - y); return x - y; };

            a.TryToCalc(5, 4);*/
            #endregion

            #region Lambdas
            /*ActiveClass activeObj2 = new ActiveClass();

            activeObj2.StartCalculation += (x, y) => { Console.WriteLine("{0} + {1} = {2}", x, y, x + y); return x + y; };
            activeObj2.StartCalculation += (x, y) => { Console.WriteLine("{0} - {1} = {2}", x, y, x - y); return x - y; };

            activeObj2.TryToCalc(5, 4);*/
            #endregion

            #region Action and Func
             /*Func<int, int, int> calc = (x, y) => { Console.WriteLine("{0} + {1} = {2}", x, y, x + y); return x + y;};
             calc += (x, y) => { Console.WriteLine("{0} - {1} = {2}", x, y, x - y); return x - y; };
             calc(5, 4);

             Action<int, int> calc_without_return = (x, y) => { Console.WriteLine("{0} + {1} = {2}", x, y, x + y); };
             calc_without_return += (x, y) => { Console.WriteLine("{0} - {1} = {2}", x, y, x - y); };
             calc_without_return(5, 4);*/
            #endregion

            #region Extension method
            Product p = new Product();
            p.Price = 1000;           
            Console.WriteLine("New price is : {0:C}", p.Discount());

            List<Product> products = new List<Product>();
            //products.
            
            products.Where(pr => { return pr.Price > 200; });

            #endregion

            Console.ReadKey();
        }
    }
}
