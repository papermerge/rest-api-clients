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
import { Node } from './node';
import { PaginatedCustomUserPreferenceListLinks } from './paginatedCustomUserPreferenceListLinks';
import { PaginatedCustomUserPreferenceListMeta } from './paginatedCustomUserPreferenceListMeta';

export class PaginatedNodeList {
    'data'?: Array<Node>;
    'meta'?: PaginatedCustomUserPreferenceListMeta;
    'links'?: PaginatedCustomUserPreferenceListLinks;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "data",
            "baseName": "data",
            "type": "Array<Node>"
        },
        {
            "name": "meta",
            "baseName": "meta",
            "type": "PaginatedCustomUserPreferenceListMeta"
        },
        {
            "name": "links",
            "baseName": "links",
            "type": "PaginatedCustomUserPreferenceListLinks"
        }    ];

    static getAttributeTypeMap() {
        return PaginatedNodeList.attributeTypeMap;
    }
}

