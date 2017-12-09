using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Gridscript : MonoBehaviour
{

    private Camera magnifyCamera;
    private GameObject magnifyBorders;
    private LineRenderer LeftBorder, RightBorder, TopBorder, BottomBorder; // Reference for lines of magnify glass borders
    private float MGOX, MG0Y; // Magnify Glass Origin X and Y position
    private float MGWidth = Screen.width / 6f, MGHeight = Screen.width / 6f; // Magnify glass width and height
    private Vector3 mousePos;

    // Use this for initialization
    IEnumerator Start()
    {
        yield return new WaitForSeconds(1f);
        Vector3 start = new Vector3(0f, 0f, 0f);
        Vector3 end = new Vector3(0f, 0f, 0f);
        Color color = Color.black;

        float width = Imageinserter.texwidth/200;
        float height = Imageinserter.texheight/200;

        float i = 0;
        while (i < 31)
        {
            float j = -1+(i / 15);
            start = new Vector3(j*width, height,-1);
            end = new Vector3(j*width, -height, -1);
            //start = new Vector3(4, height, -2);
            //end = new Vector3(4, -height, -2);
            DrawLine(start, end, color);
            i++;
            
        }

        
        float k = 0;
        while (k < 31)
        {
            float l = -1 + (k / 15);
            start = new Vector3(width, l*height, -1);
            end = new Vector3(-width, l*height, -1);
            
            DrawLine(start, end, color);
            k++;
            
        }
        
    }

    void DrawLine(Vector3 start, Vector3 end, Color color)
    {
        GameObject myLine = new GameObject();
        myLine.transform.position = start;
        myLine.AddComponent<LineRenderer>();
        LineRenderer lr = myLine.GetComponent<LineRenderer>();
        lr.material = new Material(Shader.Find("Particles/Alpha Blended Premultiply"));
        lr.SetColors(color, color);
        lr.SetWidth(0.02f, 0.02f);
        lr.SetPosition(0, start);
        lr.SetPosition(1, end);
    }


    // Update is called once per frame
    void Update()
    {

    }
}
