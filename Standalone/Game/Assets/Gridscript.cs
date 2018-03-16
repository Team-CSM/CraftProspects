using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Gridscript : MonoBehaviour
{
    public Shader shader;
    IEnumerator Start()
    {

        /// <summary>
        /// Shader asset is necessary because all shaders except ones in the assets are lost whenever game is built.
        /// 1 second delay is applied before the grid is called because the game needs time to upload the image to determine the size of the grid.
        /// Width and height is taken from the image inserter script. The grid is set to 10 by 10.
        /// </summary>

        yield return new WaitForSeconds(1f);
        Vector3 start = new Vector3(0f, 0f, 0f);
        Vector3 end = new Vector3(0f, 0f, 0f);
        Color color = Color.black;

        float width = Imageinserter.texwidth/200;
        float height = Imageinserter.texheight/200;

        float i = 0;
        while (i < 11)
        {
            float j = -1+(i / 5f);
            start = new Vector3(j*width, height,-10);
            end = new Vector3(j*width, -height, -10);
            DrawLine(start, end, color);
            i++;
            
        }
        
        float k = 0;
        while (k < 11)
        {
            float l = -1 + (k / 5f);
            start = new Vector3(width, l*height, -10);
            end = new Vector3(-width, l*height, -10);
            DrawLine(start, end, color);
            k++;
            
        }
        
    }


    /// <summary>
    /// A simple object creator takes the arguments are draws a line from start coordinates to end.
    /// </summary>

    void DrawLine(Vector3 start, Vector3 end, Color color)
    {
        GameObject myLine = new GameObject();
        myLine.transform.position = start;
        myLine.AddComponent<LineRenderer>();
        LineRenderer lr = myLine.GetComponent<LineRenderer>();
        lr.material = new Material(shader);
        lr.SetColors(color, color);
        lr.SetWidth(0.02f, 0.02f);
        lr.SetPosition(0, start);
        lr.SetPosition(1, end);
    }

    void Update()
    {

    }
}
