/**
 * Papermerge REST API
 * Document management system designed for digital archives
 *
 * The version of the OpenAPI document: 2.1.0b12
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

export class PagesMoveToFolder {
    'pages': Array<string>;
    'dst': string;
    'singlePage'?: boolean = false;
    'titleFormat'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "pages",
            "baseName": "pages",
            "type": "Array<string>"
        },
        {
            "name": "dst",
            "baseName": "dst",
            "type": "string"
        },
        {
            "name": "singlePage",
            "baseName": "single_page",
            "type": "boolean"
        },
        {
            "name": "titleFormat",
            "baseName": "title_format",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return PagesMoveToFolder.attributeTypeMap;
    }
}
